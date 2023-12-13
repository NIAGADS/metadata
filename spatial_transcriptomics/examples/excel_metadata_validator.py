#! /usr/bin/env python3
import logging
import argparse
from os import path, getcwd

from niagads.utils.logging import ExitOnExceptionHandler
from niagads.validators import MetadataValidator, FileManifestValidator
from niagads.utils.dict import print_dict
from niagads.utils.string import xstr

logger = logging.getLogger(__name__)

def validate_metadata(worksheet):
    schema = path.join(args.schemaDir, worksheet + ".json")
    validator = MetadataValidator(args.excelFile, schema, args.debug)
    validator.load(worksheet)
    if args.debug:
        logger.debug(print_dict(validator.get_metadata_object(), pretty=True))
    return validator.run(failOnError=args.failAtFirst)
    
def run():
    try:
        errors = {}
        for worksheet in ['project', 'experiment_metadata']:
            validationResult = validate_metadata(worksheet)
            logger.debug(validationResult)
            errors[worksheet] = "PASSED" if isinstance(validationResult, bool) else validationResult
            
        fmSchema = path.join(args.schemaDir, 'file_manifest.json')
        fmValidator = FileManifestValidator(args.excelFile, fmSchema, args.debug)
        fmValidator.load('file_manifest')
        if args.debug:
            logger.debug(print_dict(fmValidator.get_metadata_object(), pretty=False))
        validationResult = fmValidator.run(failOnError=args.failAtFirst)
        errors['file_manifest'] = "PASSED" if isinstance(validationResult, bool) else validationResult

        logger.info("DONE")
        logger.info(print_dict(errors, pretty=True))
    except Exception as err:
        logger.exception(err)

if __name__ == "__main__":
    argParser = argparse.ArgumentParser(description="EXCEL to JSON w/Validation test", allow_abbrev=False)
    argParser.add_argument('--excelFile', help="EXCEL file name (full path)", required=True)
    argParser.add_argument('--schemaDir', help="full path to directory containing schema files", required=True)
    argParser.add_argument('--failAtFirst', action='store_true')
    argParser.add_argument('--debug', action='store_true')
    
    args = argParser.parse_args()

    logging.basicConfig(
            handlers=[ExitOnExceptionHandler(
                filename=path.join(getcwd(), 'EXCEL_validation_test.log'),
                mode='w',
                encoding='utf-8',
            )],
            format='%(asctime)s %(funcName)s %(levelname)-8s %(message)s',
            level=logging.DEBUG)
    
    run()
    
    

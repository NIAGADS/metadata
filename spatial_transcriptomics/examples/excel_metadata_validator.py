#! /usr/bin/env python3
import logging
import argparse
from os import path, getcwd

from niagads.utils.logging import ExitOnExceptionHandler
from niagads.validators import MetadataValidator, FileManifestValidator, BiosourcePropertiesValidator
from niagads.utils.dict import print_dict

logger = logging.getLogger(__name__)

def validate_metadata(worksheet):
    schema = path.join(args.schemaDir, worksheet + ".json")
    validator = MetadataValidator(args.excelFile, schema, args.debug)
    validator.load(worksheet)
    if args.debug:
        logger.debug(print_dict(validator.get_metadata(), pretty=True))
    return validator.run(failOnError=args.failAtFirst)
    
def run():
    try:
        errors = {}
        for worksheet in ['project', 'experiment_metadata']:
            validationResult = validate_metadata(worksheet)
            errors[worksheet] = "PASSED" if isinstance(validationResult, bool) else validationResult

        # TODO Biosource properties validation
        # schema = path.join(args.schemaDir, 'biosource_properties.json')
        # bsValidator = BiosourcePropertiesValidator(args.excelFile, schema, args.debug)
        # bsValidator.load('biosource_properties')
        # if args.debug:
        #     logger.debug(print_dict(bsValidator.get_metadata(), pretty=False))
        # validationResult = bsValidator.run(failOnError=args.failAtFirst)
        # errors['biosource_properties'] = "PASSED" if isinstance(validationResult, bool) else validationResult
        # validSampleIds = bmValidator.get_sample_ids()
         
        schema = path.join(args.schemaDir, 'file_manifest.json')
        fmValidator = FileManifestValidator(args.excelFile, schema, args.debug)
        fmValidator.load('file_manifest')
        if args.debug:
            logger.debug(print_dict(fmValidator.get_metadata(), pretty=False))
        validationResult = fmValidator.run(failOnError=args.failAtFirst)
        errors['file_manifest'] = "PASSED" if isinstance(validationResult, bool) else validationResult

        # TODO file manifest sample id validation
        # fmValidator.validate_samples('sample_id', validSamples)
        
        logger.info("DONE")
        logger.info(print_dict(errors, pretty=True))
    except Exception as err:
        logger.exception(err)

if __name__ == "__main__":
    argParser = argparse.ArgumentParser(description="EXCEL to JSON w/Validation test", allow_abbrev=False)
    argParser.add_argument('--excelFile', help="EXCEL file name (full path)", required=True)
    argParser.add_argument('--schemaDir', help="full path to directory containing schema files", required=True)
    argParser.add_argument('--logFile', help="log file name, saves to current working directory", 
        default="EXCEL_validation_test.log")
    argParser.add_argument('--failAtFirst', action='store_true')
    argParser.add_argument('--debug', action='store_true')
    
    args = argParser.parse_args()

    logging.basicConfig(
            handlers=[ExitOnExceptionHandler(
                filename=path.join(getcwd(), args.logFile),
                mode='w',
                encoding='utf-8',
            )],
            format='%(asctime)s %(funcName)s %(levelname)-8s %(message)s',
            level=logging.DEBUG)
    
    run()
    
    

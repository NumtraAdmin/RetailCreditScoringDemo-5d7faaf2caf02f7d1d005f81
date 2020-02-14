import traceback
import sys
from operations import TopOperation
from operations import JoinOperation
from operations import AggregationOperation
from operations import FormulaOperation
from operations import FilterOperation
from connectors import DBFSConnector
from connectors import CosmosDBConnector
from datatransformations import TranformationsMainFlow
from automl import tpot_execution
from core import PipelineNotification
import json

try: 
	PipelineNotification.PipelineNotification().started_notification('5d80e907b276bfcc57d2e600','5e26b8e42fb16412176c3a5d','http://104.42.172.209:3200/pipeline/notify')
	retail_source_01 = DBFSConnector.DBFSConnector.fetch([], {}, "5d80e907b276bfcc57d2e600", spark, "{'url': '/Demo/RetailCreditScoringTrain.csv', 'file_type': 'Delimeted', 'dbfs_token': 'dapi2936395fb3cbcb995e4fe803cc653542', 'dbfs_domain': 'westus.azuredatabricks.net', 'delimiter': ',', 'is_header': 'Use Header Line'}")

	PipelineNotification.PipelineNotification().completed_notification('5d80e907b276bfcc57d2e600','5e26b8e42fb16412176c3a5d','http://104.42.172.209:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5d80e907b276bfcc57d2e600','5e26b8e42fb16412176c3a5d','http://104.42.172.209:3200/pipeline/notify','http://104.42.172.209:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5d80edfb935866d26888d2ee','5e26b8e42fb16412176c3a5d','http://104.42.172.209:3200/pipeline/notify')
	retail_fe = TranformationsMainFlow.TramformationMain.run(["5d80e907b276bfcc57d2e600"],{"5d80e907b276bfcc57d2e600": retail_source_01}, "5d80edfb935866d26888d2ee", spark,json.dumps( {"FE": [{"transformationsData": {}, "feature": "Creditability", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1000", "mean": "0.7", "stddev": "0.46", "min": "0", "max": "1", "missing": "0"}}, {"transformationsData": {}, "feature": "Account_Balance", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1000", "mean": "2.58", "stddev": "1.26", "min": "1", "max": "4", "missing": "0"}}, {"transformationsData": {}, "feature": "Duration_of_Credit(month)", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1000", "mean": "20.9", "stddev": "12.06", "min": "4", "max": "72", "missing": "0"}}, {"transformationsData": {}, "feature": "Payment_Status_of_Previous_Credit", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1000", "mean": "2.54", "stddev": "1.08", "min": "0", "max": "4", "missing": "0"}}, {"transformationsData": {}, "feature": "Purpose", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1000", "mean": "2.83", "stddev": "2.74", "min": "0", "max": "10", "missing": "0"}}, {"transformationsData": {}, "feature": "Credit_Amount", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1000", "mean": "3271.25", "stddev": "2822.75", "min": "250", "max": "18424", "missing": "0"}}, {"transformationsData": {}, "feature": "Value_Savings_Stocks", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1000", "mean": "2.1", "stddev": "1.58", "min": "1", "max": "5", "missing": "0"}}, {"transformationsData": {}, "feature": "Length_of_current_employment", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1000", "mean": "3.38", "stddev": "1.21", "min": "1", "max": "5", "missing": "0"}}, {"transformationsData": {}, "feature": "Instalment_per_cent", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1000", "mean": "2.97", "stddev": "1.12", "min": "1", "max": "4", "missing": "0"}}, {"transformationsData": {}, "feature": "Sex_&_Marital_Status", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1000", "mean": "2.68", "stddev": "0.71", "min": "1", "max": "4", "missing": "0"}}, {"transformationsData": {}, "feature": "Guarantors", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1000", "mean": "1.15", "stddev": "0.48", "min": "1", "max": "3", "missing": "0"}}, {"transformationsData": {}, "feature": "Duration_in_Current_address", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1000", "mean": "2.85", "stddev": "1.1", "min": "1", "max": "4", "missing": "0"}}, {"transformationsData": {}, "feature": "Most_valuable_available_asset", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1000", "mean": "2.36", "stddev": "1.05", "min": "1", "max": "4", "missing": "0"}}, {"transformationsData": {}, "feature": "Age(years)", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1000", "mean": "35.54", "stddev": "11.35", "min": "19", "max": "75", "missing": "0"}}, {"transformationsData": {}, "feature": "Concurrent_Credits", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1000", "mean": "2.67", "stddev": "0.71", "min": "1", "max": "3", "missing": "0"}}, {"transformationsData": {}, "feature": "Type_of_apartment", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1000", "mean": "1.93", "stddev": "0.53", "min": "1", "max": "3", "missing": "0"}}, {"transformationsData": {}, "feature": "No_of_Credits_at_this_Bank", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1000", "mean": "1.41", "stddev": "0.58", "min": "1", "max": "4", "missing": "0"}}, {"transformationsData": {}, "feature": "Occupation", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1000", "mean": "2.9", "stddev": "0.65", "min": "1", "max": "4", "missing": "0"}}, {"transformationsData": {}, "feature": "No_of_dependents", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1000", "mean": "1.16", "stddev": "0.36", "min": "1", "max": "2", "missing": "0"}}, {"transformationsData": {}, "feature": "Telephone", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1000", "mean": "1.4", "stddev": "0.49", "min": "1", "max": "2", "missing": "0"}}, {"transformationsData": {}, "feature": "Foreign_Worker", "transformation": "", "type": "numeric", "replaceby": "mean", "selected": "True", "stats": {"count": "1000", "mean": "1.04", "stddev": "0.19", "min": "1", "max": "2", "missing": "0"}}]}))

	PipelineNotification.PipelineNotification().completed_notification('5d80edfb935866d26888d2ee','5e26b8e42fb16412176c3a5d','http://104.42.172.209:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5d80edfb935866d26888d2ee','5e26b8e42fb16412176c3a5d','http://104.42.172.209:3200/pipeline/notify','http://104.42.172.209:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5d8104f8935866d26888d3ac','5e26b8e42fb16412176c3a5d','http://104.42.172.209:3200/pipeline/notify')
	retail_autoMl = tpot_execution.Tpot_execution.run(["5d80edfb935866d26888d2ee"],{"5d80edfb935866d26888d2ee": retail_fe}, "5d8104f8935866d26888d3ac", spark,json.dumps( {"model_type": "classification", "label": "Creditability", "features": ["Account_Balance", "Duration_of_Credit(month)", "Payment_Status_of_Previous_Credit", "Purpose", "Credit_Amount", "Value_Savings_Stocks", "Length_of_current_employment", "Instalment_per_cent", "Sex_&_Marital_Status", "Guarantors", "Duration_in_Current_address", "Most_valuable_available_asset", "Age(years)", "Concurrent_Credits", "Type_of_apartment", "No_of_Credits_at_this_Bank", "Occupation", "No_of_dependents", "Telephone", "Foreign_Worker"], "percentage": "10", "executionTime": "5", "sampling": "1", "sampling_value": "over", "run_id": "e4eded5638774eb39ad8dc5b370e2686", "model_id": "5e46a5418932993838ab5c43", "ProjectName": "ML Scenarios", "PipelineName": "RetailCreditScoringDemo", "userid": "5e26b8e42fb16412176c3a5d", "runid": "", "url_ResultView": "http://104.42.172.209:3200", "experiment_id": "551308251382540"}))

	PipelineNotification.PipelineNotification().completed_notification('5d8104f8935866d26888d3ac','5e26b8e42fb16412176c3a5d','http://104.42.172.209:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5d8104f8935866d26888d3ac','5e26b8e42fb16412176c3a5d','http://104.42.172.209:3200/pipeline/notify','http://104.42.172.209:3200/logs/getProductLogs')
	sys.exit(1)


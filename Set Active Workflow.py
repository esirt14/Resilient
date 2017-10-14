#Get Incident Types
  
#incident.incident_type_ids

tmp = ''
sActiveWorkflow = ''
dActiveWorkflow = []

sActiveWorkflow = str(incident.properties.active_workflow)
sIncidentTypeIds = str(incident.incident_type_ids)
#log.info(sActiveWorkflow)
#log.info(sIncidentTypeIds)
#log.info(incident.phase_id)
#log.info(task.name)

if "Initial Triage" in incident.properties.active_workflow:
  if incident.phase_id <> "Triage" and incident.phase_id <> "Pre-Checks":
    #log.info("Yes")
    #log.info(sActiveWorkflow)
    tmp = sActiveWorkflow.replace(", Initial Triage", "").replace("Initial Triage, ", "").replace("Initial Triage", "")
    #log.info(sActiveWorkflow)
    tmp = tmp.replace('[', '').replace(']', '')
    tmp = tmp.replace(' ,', ',').replace(', ', ',')
    #log.info('Tmp is :')
    #log.info(tmp)
    dActiveWorkflow = tmp.split(',')
    log.info('dActiveWorkflow is :')
    log.info(str(dActiveWorkflow))
    if "" in dActiveWorkflow:
      #log.info('Hit')
      incident.properties.active_workflow = []
      tmp = ''
      sActiveWorkflow = str(incident.properties.active_workflow)
      dActiveWorkflow = []
    else:
      #log.info('No hit')
      #log.info(sActiveWorkflow)
      #log.info(str(dActiveWorkflow))
      incident.properties.active_workflow = dActiveWorkflow
      tmp = ''
      sActiveWorkflow = str(incident.properties.active_workflow)
      dActiveWorkflow = []
    log.info(str(incident.properties.active_workflow))
else:
  log.info("Initial Triage is already complete")
  
#log.info(tmp)
#log.info(sActiveWorkflow)
#log.info(str(dActiveWorkflow))

if "Malware" in incident.incident_type_ids and "Malware" not in incident.properties.active_workflow:
  sActiveWorkflow = str(incident.properties.active_workflow)
  if "" in incident.properties.active_workflow:
    tmp = sActiveWorkflow.replace('[]', 'Malware')
    dActiveWorkflow = tmp.split(',')
    #log.info(str(dActiveWorkflow))
    incident.properties.active_workflow = dActiveWorkflow
    tmp = ''
    sActiveWorkflow = str(incident.properties.active_workflow)
    dActiveWorkflow = []
  else:
    tmp = sActiveWorkflow.replace(']', ', Malware]')
    tmp = tmp.replace('[', '').replace(']', '')
    tmp = tmp.replace(' ,', ',').replace(', ', ',')
    log.info(tmp)
    dActiveWorkflow = tmp.split(',')
    log.info(str(dActiveWorkflow))
    incident.properties.active_workflow = dActiveWorkflow
    tmp = ''
    sActiveWorkflow = str(incident.properties.active_workflow)
    dActiveWorkflow = []
else:
  log.info("Incident Type of Malware not applied or workflow is already active")

#log.info(incident.incident_type_ids)

#if(incident.active_workflow)

def get_class_file_contents():
    return """
import datetime

from taupatias_back.diagnosis_prediction.domain.patient_data import PatientData


class Diagnosis:
    def __init__(self, id_: str, patient_data: PatientData, diagnosis: str, comments: str,
                 creation_date: datetime.datetime):
        self.id_ = id_
        self.patient_data = patient_data
        self.diagnosis = diagnosis
        self.comments = comments
        self.creation_date = creation_date
    """

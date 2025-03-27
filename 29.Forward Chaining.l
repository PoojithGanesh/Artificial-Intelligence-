% Facts: Symptoms of diseases
symptom(patient, fever).
symptom(patient, cough).
symptom(patient, headache).
symptom(patient, fatigue).
symptom(patient, rash).
symptom(patient, sore_throat).

% Rules: Diseases based on symptoms
disease(patient, flu) :- 
    symptom(patient, fever), 
    symptom(patient, cough), 
    symptom(patient, headache).

disease(patient, covid) :- 
    symptom(patient, fever), 
    symptom(patient, cough), 
    symptom(patient, fatigue), 
    symptom(patient, sore_throat).

disease(patient, measles) :- 
    symptom(patient, fever), 
    symptom(patient, rash), 
    symptom(patient, cough).

% Query examples
% To check if the patient has flu:
% ?- disease(patient, flu).

% To find all possible diseases:
% ?- disease(patient, X).
X = flu ;
X = covid ;
X = measles.


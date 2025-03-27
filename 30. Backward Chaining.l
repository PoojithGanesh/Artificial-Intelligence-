% Facts: Symptoms of diseases
symptom(flu, fever).
symptom(flu, cough).
symptom(flu, headache).
symptom(cold, cough).
symptom(cold, sneezing).
symptom(covid, fever).
symptom(covid, cough).
symptom(covid, loss_of_taste).
symptom(malaria, fever).
symptom(malaria, chills).

% Rule: Diagnose a disease based on at least two matching symptoms
has_disease(Patient, Disease) :-
    symptom(Disease, S1),
    symptom(Disease, S2),
    S1 \= S2,  % Ensure different symptoms
    write(Patient), write(' may have '), write(Disease), nl,
    fail.  % Force backtracking to find all possible diseases

% To prevent Prolog from returning 'false' after backtracking
has_disease(_, _).

Query:
% ?- has_disease(john, Disease).

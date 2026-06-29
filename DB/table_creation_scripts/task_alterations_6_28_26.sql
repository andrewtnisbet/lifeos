alter table tasks
add column classification_confidence numeric(3,2) default 0.0;

alter table tasks
add column capture_source text default 'manual';
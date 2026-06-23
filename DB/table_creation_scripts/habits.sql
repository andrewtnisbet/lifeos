create table habits (
  id uuid primary key default gen_random_uuid(),

  responsibility_id uuid references responsibilities(id),

  name text,

  frequency text,

  target_per_week integer,

  streak integer default 0,

  created_at timestamptz default now()
);
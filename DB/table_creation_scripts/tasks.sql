create table tasks (
  id uuid primary key default gen_random_uuid(),

  project_id uuid references projects(id),

  title text not null,

  description text,

  status text default 'open',

  priority integer default 5,

  estimated_minutes integer,

  actual_minutes integer,

  due_date date,

  energy_required text,

  can_split boolean default true,

  preferred_time_of_day text,

  must_schedule boolean default false,

  recurrence_rule text,

  last_touched timestamptz default now(),

  created_at timestamptz default now(),

  updated_at timestamptz default now()
);
create table attention_allocation (
  id uuid primary key default gen_random_uuid(),

  responsibility_id uuid references responsibilities(id),

  allocation_date date,

  minutes_allocated integer,

  source text,

  created_at timestamptz default now()
);
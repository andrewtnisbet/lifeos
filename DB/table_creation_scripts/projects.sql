create table projects (
  id uuid primary key default gen_random_uuid(),

  responsibility_id uuid references responsibilities(id),

  name text not null,

  description text,

  status text default 'active',

  priority integer default 5,

  deadline date,

  estimated_total_hours numeric(6,2),

  progress_percent integer default 0,

  created_at timestamptz default now(),

  updated_at timestamptz default now()
);
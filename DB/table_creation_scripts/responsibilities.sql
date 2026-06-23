create table responsibilities (
  id uuid primary key default gen_random_uuid(),

  name text not null unique,

  description text,

  weekly_target_hours numeric(5,2),

  attention_weight integer default 5,

  health_score integer default 100,

  created_at timestamptz default now(),

  updated_at timestamptz default now()
);
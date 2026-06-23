create table daily_metrics (
  id uuid primary key default gen_random_uuid(),

  metric_date date not null,

  weight numeric(6,2),

  steps integer,

  sleep_hours numeric(4,2),

  exercise_minutes integer,

  mood integer,

  energy_level integer,

  created_at timestamptz default now()
);
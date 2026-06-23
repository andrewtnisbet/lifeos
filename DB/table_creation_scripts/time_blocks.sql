create table time_blocks (
  id uuid primary key default gen_random_uuid(),

  task_id uuid references tasks(id),

  title text,

  start_time timestamptz,

  end_time timestamptz,

  block_type text,

  status text default 'planned',

  calendar_event_id uuid references calendar_events(id),

  created_at timestamptz default now()
);
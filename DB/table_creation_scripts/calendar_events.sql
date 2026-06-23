create table calendar_events (
  id uuid primary key default gen_random_uuid(),

  external_id text,

  source text not null,

  title text,

  start_time timestamptz not null,

  end_time timestamptz not null,

  event_type text,

  is_busy boolean default true,

  created_at timestamptz default now()
);
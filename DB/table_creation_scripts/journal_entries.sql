create table journal_entries (
  id uuid primary key default gen_random_uuid(),

  entry text,

  domain text,

  mood integer,

  tags jsonb,

  created_at timestamptz default now()
);
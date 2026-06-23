create table task_dependencies (
  id uuid primary key default gen_random_uuid(),

  task_id uuid references tasks(id),

  depends_on_task_id uuid references tasks(id)
);
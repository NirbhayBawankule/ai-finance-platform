create table expenses (
  id uuid default gen_random_uuid() primary key,
  user_id uuid references auth.users(id),
  month_year text,
  category text,
  amount numeric,
  created_at timestamp default now()
);

create table predictions (
  id uuid default gen_random_uuid() primary key,
  user_id uuid references auth.users(id),
  category text,
  predicted_amount numeric,
  prediction_month text,
  created_at timestamp default now()
);

create table budgets (
  id uuid default gen_random_uuid() primary key,
  user_id uuid references auth.users(id),
  category text,
  monthly_limit numeric
);

defmodule Solution do
  def fib(1) do
    0
  end
  def fib(2) do
    1
  end
  def fib(n) do 
    fib(n-1) + fib(n-2)
  end
end

strnum = IO.gets ""
num = strnum |> String.trim("\n") |> String.to_integer

IO.puts Solution.fib(num)
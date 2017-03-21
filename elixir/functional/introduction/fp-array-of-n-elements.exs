defmodule Solution do
  def start do
    valuestr = IO.gets ""
    value = valuestr |> String.trim("\n") |> String.to_integer
    list = for n <- 1..value, do: n
    list |> IO.inspect
  end
end

Solution.start
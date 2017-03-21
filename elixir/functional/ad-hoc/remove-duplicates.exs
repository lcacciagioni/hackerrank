defmodule Solution do
  def uniques(str) do
    str |> String.codepoints |> Enum.uniq |> IO.puts
  end
end

str = IO.gets ""

Solution.uniques(str)
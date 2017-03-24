defmodule Solution do
  defp tonum(str1) do
    str1
    |> String.strip(?\n)
    |> String.to_integer
  end

  def start do
    str1 = IO.gets ""

    num1 = str1 |> tonum

    "Hello World\n"
    |> String.duplicate(num1)
    |> IO.puts
  end
end

Solution.start
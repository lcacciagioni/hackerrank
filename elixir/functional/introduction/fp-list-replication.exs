defmodule Solution do
  defp getnums(nrepeat) do
    num = IO.gets ""
    if num != :eof do
      if String.contains? num, "\n" do
        num1 = num
      else
        num1 = num <> "\n"
      end
      num1
      |> String.duplicate(nrepeat)
      |> String.trim("\n")
      |> IO.puts
      getnums(nrepeat)
    end
  end
  def start do
    firststr = IO.gets "" 
    nrepeat = firststr |> String.trim("\n") |> String.to_integer
    getnums(nrepeat)
  end
end

Solution.start
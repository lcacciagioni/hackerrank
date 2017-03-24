defmodule Solution do
  defp getnums(nrepeat) do
    num = IO.gets ""
    if num != :eof do
      if String.contains? num, "\n" do
        num
      else
        num <> "\n"
      end
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
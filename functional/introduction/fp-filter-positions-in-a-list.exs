defmodule Solution do
  require Integer
  defp printnum(count) do
    num = IO.gets ""
    if num != :eof do
      if Integer.is_even(count) do
        num
        |> String.trim("\n")
        |> IO.puts
      end
      printnum(count + 1)
    end
  end
  
  def start do
    printnum(1)
  end
end

Solution.start
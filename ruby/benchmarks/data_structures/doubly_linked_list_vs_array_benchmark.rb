# frozen_string_literal: true

require "bundler/setup"
require "algorithms"
require "benchmark/ips"

puts "****Benchmark push****"
Benchmark.ips do |x|
  x.config(time: 1, warmup: 0)

  x.report("doubly_linked_list") do
    dll = DataStructures::DoublyLinkedList.new
    1_000_000.times do |n|
      dll << n
    end
  end

  x.report("array") do
    l = []
    1_000_000.times do |n|
      l << n
    end
  end

  x.compare!
end

puts "****Benchmark pop****"
Benchmark.ips do |x|
  x.config(time: 1, warmup: 0)

  dll = DataStructures::DoublyLinkedList.new
  1_000_000.times { |n| dll << n }
  x.report("doubly_linked_list") do
    1_000_000.times { dll.pop }
  end

  l = []
  1_000_000.times { |n| l << n }
  x.report("array") do
    1_000_000.times { l.pop }
  end

  x.compare!
end

puts "****Benchmark unshift****"
Benchmark.ips do |x|
  x.config(time: 1, warmup: 0)

  x.report("doubly_linked_list") do
    dll = DataStructures::DoublyLinkedList.new
    1_000_000.times do |n|
      dll.unshift(n)
    end
  end

  x.report("array") do
    l = []
    1_000_000.times do |n|
      l.unshift(n)
    end
  end

  x.compare!
end

puts "****Benchmark shift****"
Benchmark.ips do |x|
  x.config(time: 1, warmup: 0)

  dll = DataStructures::DoublyLinkedList.new
  1_000_000.times { |n| dll << n }
  x.report("doubly_linked_list") do
    1_000_000.times { dll.shift }
  end

  l = []
  1_000_000.times { |n| l << n }
  x.report("array") do
    1_000_000.times { l.shift }
  end

  x.compare!
end

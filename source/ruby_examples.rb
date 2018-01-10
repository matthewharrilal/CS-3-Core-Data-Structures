def calc(first, second)
    return first * second
end


module MyModule
    def print_hello
        puts "Hello"
    end
end


class Human
    # def initalize(name, age)
    #     @name = name
    #     @age = age
    # end

    # def name()
    #     @name
    # end 

    # def name=(new_name)
    #     @name = new_name
    # end

    # One @ is an instance variable and two is a class variable

    attr_accessor :name, :age, :specie_name
    @@specie_name = "Mamalia"

    def initalize(name, age)
        @name = name
        @age = age
    end

    def specie_name()
        @@specie_name
    end

    def returns_name()
        puts "Hello world"
    end
end
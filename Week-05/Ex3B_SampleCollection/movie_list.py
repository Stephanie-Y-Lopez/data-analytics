#Stephanie Y. Lopez Chavoya
movie_list = ["The book of life", "Jurassic series", "Fast and Furious series", "Twilight series", "Shrek"]

#lens function
print(f"The list movie_list includes my top {len(movie_list)} favorite movies/movie series.")
print(movie_list)
print("-" * 95)

#sort function 
print("Sorted temporarily with sorted():")
print(sorted(movie_list))

print(movie_list)
print("-" * 95)

movie_list.sort()
print("Sorted with .sort():")
print(movie_list)
print("-" * 95)

# 5. Add a new movie using .append() and print updated statement + list
movie_list.append("Beauty and the Beast")
print(f"The list movie_list now includes my top {len(movie_list)} favorite movies.")
print(movie_list)
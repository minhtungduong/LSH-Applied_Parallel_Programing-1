from datasketch import MinHash, MinHashLSH

# Dữ liệu mẫu
movies = {
    "Toy Story": ["animation", "comedy", "family"],
    "Finding Nemo": ["animation", "adventure", "family"],
    "The Lion King": ["animation", "drama", "musical"],
    "The Godfather": ["crime", "drama"],
}

# Số lượng permutation
num_perm = 128

# Tạo MinHash cho mỗi bộ phim
minhashes = {}
for movie, tags in movies.items():
    m = MinHash(num_perm=num_perm)
    for tag in tags:
        m.update(tag.encode('utf8'))
    minhashes[movie] = m

# Tạo LSH index
lsh = MinHashLSH(threshold=0.5, num_perm=num_perm)
for movie, m in minhashes.items():
    lsh.insert(movie, m)

# Truy vấn
query_movie = "Toy Story"
result = lsh.query(minhashes[query_movie])
print("Các bộ phim tương tự với", query_movie, ":", result)

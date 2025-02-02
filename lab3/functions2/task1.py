movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def check(movies):
    name = input("Enter the movie title: ")
    for movie in movies:
        if movie['name'].lower() == name.lower():
            return movie['imdb'] > 5.5
    return False  
#print(check(movies))  


def high_rate(movies):
    l = [x for x in movies if x['imdb'] > 5.5]
    for x in l:
        print(x)

#high_rate(movies)


def categ(movies):
    name = input("Enter the categoty of movie: ")
    for movie in movies:
        if movie["category"].lower() == name.lower():
            print(movie)

#categ(movies)
            

def avarage(movies):
    cnt = 0
    for movie in movies:
        cnt += movie["imdb"]
    return cnt/len(movies)

#print(avarage(movies))


def categ_score(movies):
    name = input("Enter the categoty of movie: ")
    cnt = 0
    t = 0
    for movie in movies:
        if movie["category"].lower() == name.lower():
            cnt += movie["imdb"]
            t += 1
    return cnt/t

#print(categ_score(movies))

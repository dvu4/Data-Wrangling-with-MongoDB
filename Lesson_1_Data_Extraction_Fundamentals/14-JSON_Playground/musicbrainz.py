# To experiment with this code freely you will have to run this code locally.
# We have provided an example json output here for you to look at,
# but you will not be able to run any queries through our UI.
import json
import requests


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data


def main():
    # Question 1 : How many bands named "First Aid Kit" ?
    results = query_by_name(ARTIST_URL, query_type["simple"], "First Aid Kit")

    #pretty_print(results)
    
    count_First_Aid_Kit = 0

    for i in results["artists"]:
        if i["name"] == "First Aid Kit":
            count_First_Aid_Kit += 1
    print "There are {0} bands named First Aid Kit\n".format(count_First_Aid_Kit)



    # Question 2 : How many  begin_area name for "Queen" ?
    
    results = query_by_name(ARTIST_URL, query_type["simple"], "Queen")

    #pretty_print(results)

    queen = results["artists"][0]

    print "begin-area name for Queen is {0}\n".format(queen["begin-area"]["name"])



    # Question 3 : What is spanish alias for The Beatles ?
    results = query_by_name(ARTIST_URL, query_type["simple"], "The Beatles")

    #pretty_print(results)

    beatles = results["artists"][0]["aliases"] # array, list

    for i in beatles:
        if i["locale"] == "es":
            print "Spanish alias for The Beatles is {0}\n".format(i["name"])

    

    # Question 4 : What is Nirvana disambiguation ? 
    results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    
    #pretty_print(results)

    nirvana = results["artists"][0]["disambiguation"]

    print "Nirvana disambiguation is {0}\n".format(nirvana)

    # Question 5 : When was One Direction form ?
    results = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")

    #pretty_print(results)
    
    one_direction = results["artists"][0]["life-span"]

    print "One Direction form in {0}\n".format(one_direction["begin"])


    '''
    artist_id = results["artists"][1]["id"]
    print "\nARTIST:"
    pretty_print(results["artists"][1])

    artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    releases = artist_data["releases"]
    #artist_data = query_site(ARTIST_URL, query_type["aliases"], artist_id)
    #releases = artist_data["aliases"]
    print "\nONE RELEASE:"

    
    pretty_print(releases[0], indent=2)
    release_titles = [r["title"] for r in releases]
    
    print "\nALL TITLES:"
    for t in release_titles:
        print t
    '''


if __name__ == '__main__':
    main()

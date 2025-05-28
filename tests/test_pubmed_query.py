import requests

def get_pmids(query, retmax=5):
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": retmax,
        "retmode": "json"
    }
    resp = requests.get(url, params=params)
    data = resp.json()
    return data.get("esearchresult", {}).get("idlist", [])

if __name__ == "__main__":
    pmids = get_pmids("BRCA1")
    print("Got PMIDs:", pmids)


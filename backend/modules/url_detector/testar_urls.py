import pandas as pd # importando pandas
from url_detector import analisar_url # importando a função analisar_url do módulo url_detector

# testando a função analisar_url com uma lista de URLs
urls_malignas = [
    "http://117.95.20.161:56609/bin.sh",
    "http://221.202.103.35:46188/bin.sh",
    "http://222.185.171.150:44775/i",
    "http://112.248.185.61:49152/bin.sh",
    "http://222.185.171.150:44775/bin.sh",
    "http://196.191.233.24:60009/bin.sh",
    "http://42.56.212.192:55031/i",
    "http://122.157.185.197:46379/bin.sh",
    "http://182.114.32.165:37031/i",
    "http://182.114.32.165:37031/bin.sh",
    "http://196.64.168.209:49989/i",
    "http://103.167.175.121:55532/i",
    "http://196.189.198.173:42076/i",
    "http://27.37.228.145:42651/i",
    "http://222.127.243.18:35695/i"
]

urls_legitimas = [
    "https://www.microsoft.com",
    "https://www.apple.com",
    "https://www.github.com",
    "https://www.wikipedia.org",
    "https://www.amazon.com",
    "https://www.linkedin.com",
    "https://www.instagram.com",
    "https://www.reddit.com",
    "https://www.netflix.com",
    "https://www.python.org",
    "https://www.docker.com",
    "https://www.ubuntu.com",
    "https://www.mozilla.org",
    "https://www.openai.com",
    "https://www.ufersa.edu.br"
]

#for url in urls_malignas:
    #print(f"\nAnalisando a URL maligna: {url}")
    #resultado = analisar_url(url)

#for url in urls_legitimas:
    #print(f"\nAnalisando a URL legítima: {url}")
    #resultado = analisar_url(url)   

# Lista para armazenar os resultados
resultado_teste2 = []

urls_malignas_teste2 =[
    "http://59.180.138.72:54794/i", #off
    "http://79.29.100.219:58828/bin.sh", #off
    "http://220.201.27.9:47541/bin.sh",
    "http://220.201.27.9:47541/i",
    "http://60.23.239.136:47940/i",
    "http://27.215.80.81:58529/i",
    "http://78.187.104.169:56759/i",
    "http://27.207.247.91:59461/bin.sh", #off
    "http://221.14.107.151:48123/i",
    "http://219.155.201.211:50456/bin.sh",
    "http://42.228.236.172:34448/i",
    "http://27.207.246.61:38697/bin.sh",
    "http://219.155.201.211:50456/i",
    "http://60.18.98.101:50033/bin.sh",
    "http://222.127.156.105:38221/bin.sh",
    "http://222.127.156.105:38221/i",
    "http://60.18.98.101:50033/i",
    "http://222.139.194.242:60965/i",
    "http://79.29.100.219:58828/i" ,#off
    "http://60.23.238.117:50409/i" ,
    "http://222.139.194.242:60965/bin.sh",
    "http://222.137.141.81:39246/i", #off
    "http://27.207.246.61:38697/i",
    "http://42.179.150.17:56797/i",
    "http://42.59.236.181:57635/i",
    "http://39.79.68.65:34070/i",
    "http://61.137.153.247:41208/bin.sh",
    "http://42.55.227.16:40437/i",
    "http://42.179.150.17:56797/bin.sh",
    "http://61.137.192.112:51410/i",
    "http://42.59.236.181:57635/bin.sh",
    "http://61.53.75.162:37419/i",
    "http://61.53.75.162:37419/i",
    "http://78.38.18.210:38372/i",
    "http://222.127.73.15:41760/i",
    "http://93.157.253.209:56517/i",
    "http://219.154.185.65:55284/i",
    "http://175.148.80.73:34858/i",
    "http://125.44.190.92:60624/i",
    "http://203.204.93.86:35425/bin.sh",
    "http://124.234.131.24:53745/bin.sh",
    "http://203.204.93.86:35425/i",
    "http://115.56.157.204:43031/bin.sh",
    "http://115.54.126.228:48759/i",
    "http://120.28.197.69:53898/bin.sh",
    "http://122.139.13.133:53319/i",
    "http://183.151.174.249:60266/i",
    "http://196.189.69.192:55987/i",
    "http://115.55.37.155:44748/i",
    "http://124.234.219.141:44247/bin.sh"
]

urls_legitimas_teste2 = [
    "https://www.nasa.gov",
    "https://www.noaa.gov",
    "https://www.nih.gov",
    "https://www.cdc.gov",
    "https://www.whitehouse.gov",
    "https://www.congress.gov",
    "https://www.loc.gov",
    "https://www.si.edu",
    "https://www.harvard.edu",
    "https://www.mit.edu",
    "https://www.stanford.edu",
    "https://www.berkeley.edu",
    "https://www.princeton.edu",
    "https://www.yale.edu",
    "https://www.cornell.edu",
    "https://www.cam.ac.uk",
    "https://www.ox.ac.uk",
    "https://www.imperial.ac.uk",
    "https://www.ucl.ac.uk",
    "https://www.ed.ac.uk",
    "https://www.debian.org",
    "https://www.fedoraproject.org",
    "https://www.archlinux.org",
    "https://www.kernel.org",
    "https://www.gnu.org",
    "https://www.rust-lang.org",
    "https://go.dev",
    "https://nodejs.org",
    "https://www.php.net",
    "https://www.mysql.com",
    "https://www.postgresql.org",
    "https://www.sqlite.org",
    "https://kubernetes.io",
    "https://www.nginx.com",
    "https://www.apache.org",
    "https://www.blender.org",
    "https://www.libreoffice.org",
    "https://www.vim.org",
    "https://www.raspberrypi.com",
    "https://www.arduino.cc",
    "https://www.cloudflare.com",
    "https://www.digitalocean.com",
    "https://www.heroku.com",
    "https://www.twilio.com",
    "https://www.dropbox.com",
    "https://www.trello.com",
    "https://slack.com",
    "https://zoom.us",
    "https://www.canva.com",
    "https://www.gov.br"
]

for url in urls_malignas_teste2:
    resultado = analisar_url(url)

    linha = {
        "Classificação": "Maligna",
        "URL": url,
        "Malicious": resultado["malicious"],
        "Suspicious": resultado["suspicious"],
        "Undetected": resultado["undetected"],
        "Harmless": resultado["harmless"],
        "Timeout": resultado["timeout"]
    }

    resultado_teste2.append(linha)

for url in urls_legitimas_teste2:
    resultado = analisar_url(url)

    linha = {
            "Classificação": "Legitima",
            "URL": url,
            "Malicious": resultado["malicious"],
            "Suspicious": resultado["suspicious"],
            "Undetected": resultado["undetected"],
            "Harmless": resultado["harmless"],
            "Timeout": resultado["timeout"]
        }
    resultado_teste2.append(linha)

# Transformando a lista em uma tabela
dados2 = pd.DataFrame(resultado_teste2)

# Salvando os resultados em CSV
dados2.to_csv("teste2.csv", index=False)


print("Análise concluída!")

# mostrando o arquivo em que os dados foram guardados
print("teste2.csv")

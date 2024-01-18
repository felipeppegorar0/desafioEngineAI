# Queries utilizadas no desafio que foram criadas através de views no banco de dados para facilitar a consulta;


# Query para responder a questão 1 na data mais recente
query_top_sectors = """
SELECT 
    y.sector_name AS Sector,
    SUM(x."Daily Position") AS PositionUSD
FROM code_challenge_felipepegoraro.source.daily_position_view x
LEFT JOIN code_challenge_felipepegoraro.source.company y ON x.company_id = y.id
WHERE POSITION_DATE IN (SELECT MAX(POSITION_DATE) FROM code_challenge_felipepegoraro.source.daily_position_view)
GROUP BY y.sector_name
ORDER BY PositionUSD DESC
LIMIT 10
"""

# Query que compões as 25 companias para responder a pergunta 2
query_top_companies_25 = """

WITH RankPrices AS (
    SELECT
        x.COMPANY_ID,
        z.close_usd,
        ROW_NUMBER() OVER (PARTITION BY x.COMPANY_ID ORDER BY z.date DESC) AS price_rank
    FROM 
        code_challenge_felipepegoraro.source.TOP25_COMPANIES_VIEW x
    LEFT JOIN code_challenge_felipepegoraro.source.PRICE z ON x.COMPANY_ID = z.company_id
),
RankShares AS (
    SELECT
        x.COMPANY_ID,
        w.shares,
        ROW_NUMBER() OVER (PARTITION BY x.COMPANY_ID ORDER BY w.date DESC) AS share_rank
    FROM 
        code_challenge_felipepegoraro.source.TOP25_COMPANIES_VIEW x
    LEFT JOIN code_challenge_felipepegoraro.source.POSITION w ON x.COMPANY_ID = w.company_id
)
SELECT
    y.ticker,
    x."media_x" AS Media,
    y.sector_name,
    p.close_usd,
    s.shares
FROM 
    code_challenge_felipepegoraro.source.TOP25_COMPANIES_VIEW x
LEFT JOIN code_challenge_felipepegoraro.source.COMPANY y ON x.company_id = y.id
LEFT JOIN RankPrices p ON x.COMPANY_ID = p.COMPANY_ID AND p.price_rank = 1
LEFT JOIN RankShares s ON x.COMPANY_ID = s.COMPANY_ID AND s.share_rank = 1

ORDER BY Media DESC;

"""

#Query com os preços tratados utilizando como base a tabela position e price para normalizar os dados e incluir datas do final de semana;
# Aqui a data dos dados foi baseada em cima da tabela position que iniciava com dados históricos a partir de 2016.


query_daily_price = """

SELECT

    Empresa_ticker,
    Setor,
    Data,
    preco_de_fechamento

FROM 
    code_challenge_felipepegoraro.source.daily_position_normalized;
"""

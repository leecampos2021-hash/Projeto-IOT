CREATE VIEW temperatura_media_por_ambiente AS
SELECT
    "room_id/id",
    AVG(temp) AS temperatura_media
FROM leituras
GROUP BY "room_id/id";

/*View 2 temperatura máxima e mínima por ambiente*/

CREATE VIEW temp_max_min_ambiente AS
SELECT "room_id/id", 
MIN(temp) as mínima, MAX(temp) as máxima
FROM leituras 
GROUP BY "room_id/id"
ORDER BY "room_id/id"

/*View 3 —quantidade de entradas e saídas*/

CREATE VIEW entradas_saidas AS
SELECT
    "out/in",
    COUNT(*) AS quantidade
FROM leituras
GROUP BY "out/in";


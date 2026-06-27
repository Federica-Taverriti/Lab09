from database.DB_connect import DBConnect
from model.aeroporto import Aeroporto
from model.rotta import Rotta


class DAO():
    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []
        query = """SELECT * 
                    FROM airports a"""

        cursor.execute(query)

        for row in cursor:
            res.append(Aeroporto(**row))

        cursor.close()
        conn.close()

        return res

    @staticmethod
    def getAllEdges(idMapA):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []
        query = """SELECT LEAST(f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) AS aeroporto1,
                        GREATEST(f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) AS aeroporto2,
                        AVG(f.DISTANCE) AS peso
                    FROM flights f 
                    GROUP BY LEAST(f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID), 
                        GREATEST(f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID)
                    ORDER BY peso"""

        cursor.execute(query)

        for row in cursor:
            res.append(Rotta(
                idMapA[row["aeroporto1"]],
                idMapA[row["aeroporto2"]],
                row["peso"]))

        cursor.close()
        conn.close()

        return res
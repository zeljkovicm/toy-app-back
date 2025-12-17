from sqlmodel import Session, text
from typing import List, Dict


class ProductRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all_products(self) -> List[Dict]:
        query = text("""
        SELECT
            p.toy_id,
            p.name,
            p.permalink,
            p.description,
            p.target_group,
            p.production_date,
            p.price,
            p.image_path AS image_url,

            ag.age_group_id,
            ag.name AS age_group_name,
            ag.description AS age_group_description,

            pt.type_id,
            pt.name AS type_name,
            pt.description AS type_description,

            COALESCE(ps.quantity, 0) AS quantity,
            COALESCE(AVG(r.rating), 0) AS average_rating,
            COUNT(r.review_id) AS review_count
        FROM product p
        JOIN age_group ag ON ag.age_group_id = p.age_group_id
        JOIN product_type pt ON pt.type_id = p.type_id
        LEFT JOIN productstock ps ON ps.toy_id = p.toy_id
        LEFT JOIN review r ON r.toy_id = p.toy_id
        GROUP BY
            p.toy_id, p.name, p.permalink, p.description,
            p.target_group, p.production_date, p.price, p.image_path,
            ag.age_group_id, ag.name, ag.description,
            pt.type_id, pt.name, pt.description,
            ps.quantity
        ORDER BY p.toy_id
        """)
        result = self.db.exec(query)
        return [dict(row) for row in result]

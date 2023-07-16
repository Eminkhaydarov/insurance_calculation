from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "rate" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "cargo_type" VARCHAR(255) NOT NULL,
    "date" DATE NOT NULL,
    "rate" DECIMAL(6,5) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """

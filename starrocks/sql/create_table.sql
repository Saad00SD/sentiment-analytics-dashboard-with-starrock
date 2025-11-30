CREATE DATABASE IF NOT EXISTS sentiment_app;
USE sentiment_app;

DROP TABLE IF EXISTS social_posts;

CREATE TABLE social_posts (
    `text`            STRING,
    `sentiment`       STRING,
    `ts`              DATETIME,
    `user`            STRING,
    `platform`        STRING,
    `hashtags`        STRING,
    `retweets`        DOUBLE,
    `likes`           DOUBLE,
    `country`         STRING,
    `year`            BIGINT,
    `month`           BIGINT,
    `day`             BIGINT,
    `hour`            BIGINT,
    `is_satisfaction` BIGINT,
    `is_complaint`    BIGINT
)
ENGINE=OLAP
DUPLICATE KEY(`text`)
DISTRIBUTED BY HASH(`text`) BUCKETS 8
PROPERTIES (
    "replication_num" = "1"
);

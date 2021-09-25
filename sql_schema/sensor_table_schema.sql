CREATE TABLE all_sensor_data
(
    utc_time_id VARCHAR(30) DEFAULT NULL,
    source_id  INT PRIMARY KEY,
    source_ref FLOAT DEFAULT NULL,
    avg_freeflow_speed FLOAT DEFAULT NULL,
    avg_travel_time FLOAT DEFAULT NULL,
    high_quality_samples FLOAT DEFAULT NULL,
    samples_below_100pct_ff FLOAT DEFAULT NULL,
    samples_below_95pct_ff FLOAT DEFAULT NULL,
    samples_below_90pct_ff FLOAT DEFAULT NULL,
    samples_below_85pct_ff FLOAT DEFAULT NULL,
    samples_below_80pct_ff FLOAT DEFAULT NULL,
    samples_below_75pct_ff FLOAT DEFAULT NULL,
    samples_below_70pct_ff FLOAT DEFAULT NULL,
    samples_below_65pct_ff FLOAT DEFAULT NULL,
    samples_below_60pct_ff FLOAT DEFAULT NULL,
    samples_below_55pct_ff FLOAT DEFAULT NULL,
    samples_below_50pct_ff FLOAT DEFAULT NULL,
    samples_below_45pct_ff FLOAT DEFAULT NULL,
    samples_below_40pct_ff FLOAT DEFAULT NULL,
    samples_below_35pct_ff FLOAT DEFAULT NULL,
    samples_below_30pct_ff FLOAT DEFAULT NULL,
    samples_below_25pct_ff FLOAT DEFAULT NULL,
    samples_below_20pct_ff FLOAT DEFAULT NULL,
    samples_below_15pct_ff FLOAT DEFAULT NULL,
    samples_below_10pct_ff FLOAT DEFAULT NULL,
    samples_below_5pct_ff FLOAT DEFAULT NULL
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
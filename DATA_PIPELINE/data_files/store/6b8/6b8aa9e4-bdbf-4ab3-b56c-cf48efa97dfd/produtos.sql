ATTACH TABLE _ UUID '5b7820bf-9810-46a2-ae01-992cf6eff516'
(
    `id` UInt32,
    `nome` String,
    `valor` Float32
)
ENGINE = MergeTree
ORDER BY id
SETTINGS index_granularity = 8192

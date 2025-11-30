SELECT 
    user,
    COUNT(*) AS total_posts,
    SUM(sentiment IN ('positive','joy','love','happy','surprise')) AS positive_posts,
    SUM(sentiment IN ('anger','sad','hate','frustration')) AS negative_posts,
    SUM(sentiment IN ('positive','joy','love','happy','surprise')) / COUNT(*) * 100 AS satisfaction_percentage,
    SUM(sentiment IN ('anger','sad','hate','frustration')) / COUNT(*) * 100 AS complaints_percentage
FROM social_posts
GROUP BY user;

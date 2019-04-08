train <- read.csv('train_data.csv')

model <- glm(td_min_b ~.,family=binomial(link='logit'),data=train)

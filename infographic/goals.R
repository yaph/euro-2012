library(ggplot2)
library(reshape2)

source('helpers.R')

df <- read.table('teams.csv', sep=',', header=TRUE, comment.char = '')

# subtract penalties so that stacked goals totals correspond to number of goals
df$Goals <- df$Goals - df$Penalty.goals
df$Team <- reorder(df$Team, df$Goals)
dfm <- melt(df[, c('Team', 'Penalty.goals', 'Goals')], id.vars=1)

ggplot(dfm, aes(x=Team, y=value)) +
    geom_bar(aes(fill=variable), position='stack') +
    coord_flip() + theme_bw() +
    opts(
        panel.grid.major=theme_blank(),
        axis.title.x=theme_blank(),
        axis.title.y=theme_blank(),
        axis.text.x=theme_text(hjust=0),
        axis.text.y=theme_text(hjust=1), # right justified
        legend.text=theme_text(),
        legend.title=theme_text()) +
    scale_fill_hue(
        c=60,
        l=60,
        name='Goals',
        breaks=c('Penalty.goals', 'Goals'),
        labels=c('Penalties', 'Total'))

ggsave(filename='goals.png')

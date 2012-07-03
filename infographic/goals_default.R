# open a device using png() and specify taget image file
png(filename="goals.png",
    width = 800, height = 600, units = "px", pointsize = 14
)

df <- read.table('teams.csv', sep=',', header=TRUE, comment.char = '')
df$Goals <- df$Goals - df$Penalty.goals

bars <- rbind(df$Penalty.goals, df$Goals)

# vertical labels: las=2, margins: mar=c(bottom, left, top, right)
par(las=2, mar=c(6, 9, 2, 2))
bp <- barplot(bars,
#    height=df$Goals,
    horiz=TRUE,
#    beside = TRUE,
    axes = FALSE,
    names.arg=df$Team,
    col=c("blue", "green"),
    legend.text = c("Penalty Goals", "Goals")
)

# close device
dev.off()

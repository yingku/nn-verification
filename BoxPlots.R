install.packages("readxl")
library("readxl")

par(mar = c(2.5,8,4,2))

data <- read_excel("NN Verification.xlsx")
boxplot(NN_Verification$A_Auc, NN_Verification$B_Auc, NN_Verification$W_Auc, 
        NN_Verification$W_ind, NN_Verification$B_ind, NN_Verification$TL_Auc,
        main = "Synthetic Data 2",
        at = c(8, 7, 6, 4, 3, 2),
        names =  c("Mixture 0","Mixture 1","Mixture 2",
                    "Independent 1","Independent 2","Transfer learning"),
        las = 2,
        col = c("black","blue", "red", "blue", "red", "green"),
        border = "black",
        horizontal = TRUE,
        notch = FALSE
)

data <- read_excel("NN Verification_2.xlsx")
boxplot(NN_Verification_2$A_Auc, NN_Verification_2$B_Auc, NN_Verification_2$W_Auc, 
        NN_Verification_2$W_ind, NN_Verification_2$B_ind, NN_Verification_2$TL_Auc,
        main = "Synthetic Data 4",
        at = c(8, 7, 6, 4, 3, 2),
        names =  c("Mixture 0","Mixture 1","Mixture 2",
                   "Independent 1","Independent 2","Transfer learning"),
        las = 2,
        col = c("black","blue", "red", "blue", "red", "green"),
        border = "black",
        horizontal = TRUE,
        notch = FALSE
)


data <- read_excel("NN Verification_3.xlsx")
boxplot(NN_Verification_3$A_Auc, NN_Verification_3$B_Auc, NN_Verification_3$W_Auc, 
        NN_Verification_3$W_ind, NN_Verification_3$B_ind, NN_Verification_3$TL_Auc,
        main = "Synthetic Data 1",
        at = c(8, 7, 6, 4, 3, 2),
        names =  c("Mixture 0","Mixture 1","Mixture 2",
                   "Independent 1","Independent 2","Transfer learning"),
        las = 2,
        col = c("black","blue", "red", "blue", "red", "green"),
        border = "black",
        horizontal = TRUE,
        notch = FALSE
)

data <- read_excel("NN Verification_4.xlsx")
boxplot(NN_Verification_4$A_Auc, NN_Verification_4$B_Auc, NN_Verification_4$W_Auc, 
        NN_Verification_4$W_ind, NN_Verification_4$B_ind, NN_Verification_4$TL_Auc,
        main = "Synthetic Data 3",
        at = c(8, 7, 6, 4, 3, 2),
        names =  c("Mixture 0","Mixture 1","Mixture 2",
                   "Independent 1","Independent 2","Transfer learning"),
        las = 2,
        col = c("black","blue", "red", "blue", "red", "green"),
        border = "black",
        horizontal = TRUE,
        notch = FALSE
)


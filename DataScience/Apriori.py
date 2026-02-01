import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

#Transaction dataset
transactions=[
    ["Bread","Milk"],
    ["Bread","Diaper","Beer","Eggs"],
    ["Milk","Diaper","Beer","Coke"],
    ["Bread","Milk","Diaper","Beer"],
    ["Bread","Milk","Diaper","Coke"]
]

te=TransactionEncoder()
te_array=te.fit(transactions).transform(transactions)
df=pd.DataFrame(te_array,columns=te.columns_)

frequent_itemsets=apriori(
    df,
    min_support=0.6,
    use_colnames=True
)

print(frequent_itemsets)

rules=association_rules(
    frequent_itemsets,
    metric="confidence",
    min_threshold=0.7
)

print(rules[["antecedents","consequents"]])
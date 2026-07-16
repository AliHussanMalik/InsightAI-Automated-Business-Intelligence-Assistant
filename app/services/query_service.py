import pandas as pd

from app.schemas.query_schema import QueryResponse

class QueryService:
    
    @staticmethod
    def answer(question: str, df: pd.DataFrame):
        
        question = question.lower().strip()
        
        numeric_columns = list(df.select_dtypes(include="number").columns)
        
        if "rows" in question:
            return QueryResponse(
                answer = f"The dataset contains {len(df)} rows."
            )
            
        if "columns" in question:
            return QueryResponse(
                answer=f"The dataset contains{len(df.columns)} columns."
            )
            
        if "columns" in question:
            return QueryResponse(
                answer = f"The dataset contains {len(df.columns)} columns."
            )
            
        if "column names" in question or "columns names" in question:
            return QueryResponse(
                answer=",".join(df.columns)
            )
            
        if "dataset size" in question:
            return QueryResponse(
                answer = f"{len(df)} rows and {len(df.columns)} columns."
            )
            
        if "missing" in question:
            missing = df.isnull().sum()
            
            text = []
            
            for col, count in missing.items():
                text.append(f"{col}: {count}")
                
            return QueryResponse(
                answer = "Missing values -> " + ",".join(text)
            )
            
        for column in numeric_columns:
            
            name = column.lower()
            
            if name in question:
                
                if "average" in question or "mean" in question:
                    
                    return QueryResponse(
                        answer = f"The average {column} is {df[column].mean():.2f}."
                    )
                    
                if "maximum" in question or "max" in question:
                    
                    return QueryResponse(
                        answr = f"The maximum {column} is {df[column].max()}."
                    )
                    
                if "minimum" in question or "min" in question:
                    
                    return QueryResponse(
                        answer=f"The minimum{column} is {df[column].min()}."
                    )
                    
                    
                if "median" in question:
                    
                    return QueryResponse(
                        answer = f"The minimum {column} is {df[column].min()}."
                    )
                    
                if "median" in question:
                    
                    return QueryResponse(
                        answer = f"The median {column} is {df[column].median()}."
                    )
                    
                if "sum" in question or "total" in question:
                    
                    return QueryResponse(
                        answer = f"The total{column} is {df[column].sum():.2f}"
                    )
                    
                if "standard deviation" in question or "std" in question:
                    
                    return QueryResponse(
                        answer = f"The variance of {column} is {df[column].var():.2f}."
                    )
                
                if "count" in question:
                    
                    return QueryResponse(
                        answer=f"There are{df[column].count()} values in {column}."
                    )
                    
                if "unique" in question:
                    for column in df.columns:
                        if column.lower() in question:
                            return QueryResponse(
                                answer=f"{column} has {df[column].unique()} unique values."
                            )
                            
                if "most common" in question:
                    
                    for column in df.columns:
                        if column.lower() in question:
                            value = df[column].mode().iloc[0]
                            
                            return QueryResponse(
                                answer=f"The most common value in{column} is '{value}'."
                            )
                            
                        return QueryResponse(
                            answer="I don't understand that question yet."
                        )
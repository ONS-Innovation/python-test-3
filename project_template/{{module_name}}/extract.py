import pandas as pd
import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


class DataExtractor:
    """Class for extracting data from various sources."""
    
    def __init__(self):
        self.supported_formats = ['.csv', '.xlsx', '.json']
    
    def extract_csv(self, file_path: str, **kwargs) -> pd.DataFrame:
        """
        Extract data from CSV file.
        
        Args:
            file_path: Path to the CSV file
            **kwargs: Additional arguments for pandas.read_csv
            
        Returns:
            DataFrame containing the extracted data
        """
        try:
            logger.info(f"Extracting data from {file_path}")
            df = pd.read_csv(file_path, **kwargs)
            logger.info(f"Successfully extracted {len(df)} rows from {file_path}")
            return df
        except Exception as e:
            logger.error(f"Error extracting data from {file_path}: {str(e)}")
            raise
    
    def validate_file_exists(self, file_path: str) -> bool:
        """
        Validate that the file exists.
        
        Args:
            file_path: Path to the file
            
        Returns:
            True if file exists, False otherwise
        """
        return Path(file_path).exists()
    
    def get_file_info(self, file_path: str) -> dict:
        """
        Get basic information about the file.
        
        Args:
            file_path: Path to the file
            
        Returns:
            Dictionary with file information
        """
        file_path = Path(file_path)
        if not file_path.exists():
            return {"exists": False}
        
        return {
            "exists": True,
            "size_bytes": file_path.stat().st_size,
            "suffix": file_path.suffix,
            "name": file_path.name
        }


def extract_from_source(source_path: str, source_type: str = "csv") -> pd.DataFrame:
    """
    Helper function to extract data from a source.
    
    Args:
        source_path: Path to the data source
        source_type: Type of source (csv, xlsx, json)
        
    Returns:
        DataFrame containing the extracted data
    """
    extractor = DataExtractor()
    
    if not extractor.validate_file_exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")
    
    if source_type.lower() == "csv":
        return extractor.extract_csv(source_path)
    else:
        raise ValueError(f"Unsupported source type: {source_type}")

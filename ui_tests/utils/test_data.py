from faker import Faker

fake = Faker()

class TestData:
    """Test için kullanılacak data class'ı"""
    
    # Valid kullanıcı bilgileri
    VALID_USERNAME = "standard_user"
    VALID_PASSWORD = "secret_sauce"
    
    # Problem kullanıcı
    PROBLEM_USERNAME = "problem_user"
    
    # Performance kullanıcı
    PERFORMANCE_USERNAME = "performance_glitch_user"
    
    # Invalid kullanıcı bilgileri
    INVALID_USERNAME = "invalid_user"
    INVALID_PASSWORD = "invalid_pass"
    
    # Locked kullanıcı
    LOCKED_USERNAME = "locked_out_user"
    
    @staticmethod
    def generate_checkout_info():
        """Random checkout bilgisi üretir"""
        return {
            "firstname": fake.first_name(),
            "lastname": fake.last_name(),
            "zipcode": fake.zipcode()
        }
    
    @staticmethod
    def get_valid_checkout_info():
        """Geçerli checkout bilgisi döner"""
        return {
            "firstname": "Enes",
            "lastname": "Okur",
            "zipcode": "06210"
        }

def get_input_int(prompt: str) -> int:
    print(prompt)
    input_int = None
    try:
        input_int = int(input())
    except Exception as e:
        print(e)
    
    return input_int
from fastapi import HTTPException, status

def raise_error_404(entity, requested_id : int):
    if not entity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Requested Data with id as {requested_id} not Found')
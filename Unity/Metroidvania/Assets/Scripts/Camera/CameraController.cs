using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraController : MonoBehaviour
{
    [Header("Target")]
    [SerializeField]
    private Transform targetTransform = null;

    private void Awake()
    {

    }

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if(targetTransform != null)
        {
            transform.position = new Vector3(
                targetTransform.position.x, 
                targetTransform.position.y, 
                transform.position.z
                );
        }
    }
}

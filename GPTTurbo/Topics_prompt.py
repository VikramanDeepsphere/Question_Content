def Sub_topics_turbo(vAR_prompt_file):
    message_log = [{"role": "system", "content": "You are a helpful assistant to Generate subtopics related to the given topic"},
                {"role": "user", "content": "Give  15 subtopics for the topic 'Data Science'"},
                    {"role": "assistant", "content": 
                                                    ''' 1. Introduction to Data Science
                                                        2. Data Wrangling and Cleaning 
                                                        3. Data Visualization 
                                                        4. Data Analysis 
                                                        5. Statistical Inference 
                                                        6. Probability Theory 
                                                        7. Linear Algebra 
                                                        8. Machine Learning 
                                                        9. Deep Learning 
                                                        10. Natural Language Processing 
                                                        11. Time Series Analysis 
                                                        12. Computer Vision 
                                                        13. Big Data Analytics 
                                                        14. Data Mining Techniques 
                                                        15. Artificial Intelligence Data Visualization Techniques
                                                                                                            '''},
                    {"role": "user", "content": "Give 5 subtopics for"+ "'"+vAR_prompt_file+"'"+" from basics"}]
    return message_log